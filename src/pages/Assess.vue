<template>
    <div>
        <v-sheet max-width="1200" class="mx-auto" elevation=4>
            <v-stepper v-model="pageIdx" style="box-shadow: none">
                <v-progress-linear
                    tile="true"
                    color="primary"
                    :value="percentDone"
                    :indeterminate="loading"
                    height=8
                    id="progressBar"
                />
                <div v-if="loading">
                    <br />
                    <h2>Loading...</h2>
                    <br />
                </div>
                <v-stepper-items>
                    <v-stepper-content
                        v-for="(page, idx) in displayPages"
                        :key="page.id"
                        :step="idx + 1"
                        class="assessment-page py-0"
                        :class="isCurrentPage(idx)"
                        @change="doFocus"
                    >
                        <v-form role="form" aria-label="questions" ref="page" lazy-validation>
                            <v-row
                                v-for="(field, index) in page.items"
                                :key="index"
                                class="assessment-item"
                            >
                                <v-col class="pt-0">
                                    <component
                                        :ref="`page${idx}_item${index}`"
                                        :id="`page${idx}_item${index}`"
                                        @responded="
                                            (selection) =>
                                                responded(selection, field.name)
                                        "
                                        @value="value"
                                        :is="field.fieldType"
                                        v-bind="field"
                                    />
                                </v-col>
                            </v-row>
                        </v-form>
                    </v-stepper-content>
                </v-stepper-items>
                <v-row class="text-center">
                    <v-col>
                        <v-btn
                            role="button" 
                            aria-label="back"
                            name="btn-back"
                            @click.native="prior"
                        >
                            <v-icon left>mdi-arrow-left-bold-circle</v-icon>
                            Back
                        </v-btn>
                        <v-btn
                            v-if="finished"
                            role="button" 
                            aria-label="finish"
                            color="success"
                            name="btn-finish"
                            @click="finish"
                        >
                            Next
                            <v-icon>mdi-arrow-right-bold-circle</v-icon>
                        </v-btn>
                        <v-btn
                            v-else
                            role="button" 
                            aria-label="next"
                            color="success"
                            name="btn-next"
                            @click.native="next"
                        >
                            Next
                            <v-icon>mdi-arrow-right-bold-circle</v-icon>
                        </v-btn>
                    </v-col>
                </v-row>
            </v-stepper>
        </v-sheet>
    </div>
</template>

<script>
import SmallTextInput from "../components/controls/SmallTextInput.vue";
import SingleChoiceInput from "../components/controls/SingleChoiceInput.vue";
import MultipleChoiceInput from "../components/controls/MultipleChoiceInput.vue";
import BooleanInput from "../components/controls/BooleanInput.vue";
import Stimulus from "../components/controls/Stimulus.vue";
import utils from "@/js/assess-utils.js";

export default {
    name: "Assess",
    self: this,
    props: ["journeys"],
    components: {
        "small-text-input": SmallTextInput,
        "single-choice-input": SingleChoiceInput,
        "multiple-choice-input": MultipleChoiceInput,
        "boolean-input": BooleanInput,
        stimulus: Stimulus,
    },
    beforeDestroy() {
        this.$store.commit('setJourney', null)
    },
    created() {
        fetch(this.endpoint + "/journey", {
            method: "post",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ journeys: this.journeys }),
        })
            .then((x) => x.json())
            .then((x) => {
                this.fields = x;
            })
            .then(() => {
                // Create page structures that will calculate the required journeys for an assessment
                this.loading = false;
                this.pageIdx = 1;
                this.emitJourney();
                this.doFocus();
            });
    },
    computed: {
        completed() {
            return this.$store.getters.staticContent("COMPLETED")
        },
        percentDone() {
            return Math.round((this.pageIdx / this.displayPages.length) * 100);
        },
        finished() {
            return !this.displayPages.slice(this.pageIdx).some(page => page.items && page.items.length);
        },
        displayPages() {
            // Arguably, this should filter the pages but it'd make progress tracking harder
            let self = this;

            if (!this.fields.pages) return [{}];

            return this.fields.pages.map(function(pg) {
                let newPg = Object.assign({}, pg);

                newPg.items = pg.items.filter(
                    (x) =>
                        !utils.intersects(x.excludeTags, self.tags) &&
                        (utils.intersects(x.includeTags, self.tags) ||
                            (x.includeTags || []).length === 0)
                );

                return newPg;
            });
        },
    },
    methods: {
        next() {
            // Validate that items on the page contain responses
            let page_valid = this.$refs.page[this.pageIdx - 1].validate();
            if (!page_valid) {
                return;
            }
            // navigates to the next page
            this.movePage(true);
        },
        prior() {                    
            if (this.pageIdx > 1) {
                this.movePage(false);
            } else {
                this.$router.push({
                    name: "Select"
                })
            }
        },
        pageEmpty() {
            return this.displayPages[this.pageIdx - 1].items.length < 1;
        },
        movePage(forwards) {
            // check if a dialog needs to be displayed to the user
            if (this.proceedDialog()) {
                return;
            }

            if (forwards) this.pageIdx++;
            else this.pageIdx--;

            if (this.pageEmpty()) this.movePage(forwards);
            this.emitJourney();
            this.doFocus();
        },
        doFocus(){
            window.scrollTo(0,0);
            this.$nextTick(()=> {
                this.$refs[`page${this.pageIdx-1}_item0`][0].focus()
            })
            
        },
        emitJourney() {
            this.$store.commit('setJourney', this.$data.fields.pages[this.pageIdx-1].journey)
        },
        responded(selection, name) {
            var response = {
                name: name,
                choices: selection,
            };
            var currentResponseIndex = this.responses.findIndex(
                (response) => response.name === name
            );
            if (currentResponseIndex >= 0) {
                this.responses[currentResponseIndex] = response;
            } else {
                this.responses.push(response);
            }

            this.tags = this.responses
                .flatMap((x) => x.choices)
                .flatMap((x) => x.tags);
        },
        isCurrentPage(idx) {
            return idx + 1 == this.pageIdx ? `current` : null;
        },
        finish() {
            let valid = this.$refs.page[this.pageIdx - 1].validate()
            // Validate page
            if (!valid) {
                console.log("page invalid");
                return;
            }
            console.log("page valid");
            // check if a dialog needs to be displayed to the user
            if (this.proceedDialog()) {
                return;
            }

            if (valid) {
                this.$dialog
                    .display(
                        this.completed.title,
                        this.completed.content,
                        [{text:'View my results', color:'success'}, {text:'Cancel',color:''}]
                    )
                    .then((result) => {
                        console.log(result)
                        if (result === 0) return this.$router.push({ name: "Result", params: { responses: this.responses } });
                        if (result === 1) return this.doFocus();
                    })
            }
        },
        proceedDialog() {
            const choice = this.responses
                .flatMap((response) => response.choices)
                .find((choice) => "dialog" in choice);

            if (choice && "dialog" in choice) {
                this.$dialog
                    .fullscreen(
                        choice.dialog.title,
                        choice.dialog.content
                    ).then(()=> this.doFocus())
                return true;
            }
            return false;
        },
        //kill
        availableJourneys() {
            let choices = [];
            let tags = utils.getResponseTags(this.responses);
            this.journeys.forEach((j) => {
                if (
                    tags.some((tag) => {
                        return tag === j.parent;
                    })
                ) {
                    let choice = {
                        value: j.label,
                        parent: j.parent,
                        doc: j.doc,
                    };
                    choices.push(choice);
                }
            });
            return choices;
        },
        journeyParents() {
            let choices = [];
            this.journeys.forEach((j) => {
                let addChoice = choices.some((choice) => {
                    return choice.value === j.parent;
                });
                if (!addChoice) {
                    choices.push({ value: j.parent, tags: [j.parent] });
                }
            });
            return choices;
        },
        value(v) {
            console.log("invoked value():", v);
        },
    },
    data() {
        return {
            loading: true,
            fields: {},
            pageIdx: 0,
            responses: [],
            tags: [], // this is here to allow quick assessment mutations but I suspect that you
            // could achieve the same by watching `responses`
            endpoint: process.env.VUE_APP_API_ENDPOINT,
        };
    },
};
</script>