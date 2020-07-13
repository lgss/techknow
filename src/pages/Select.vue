<template>
    <div>
        <v-sheet max-width="1200" class="mx-auto" elevation=4>
            <v-progress-linear value="0"></v-progress-linear>
            <v-container class="v-stepper__items">
                <v-container class="v-stepper__content">
                    <v-skeleton-loader v-show="loading" type="card" />

                    <v-form role="form" aria-label="Your journey" ref="categories" v-show="!loading && !showJourneys">
                        <v-row>
                            <v-col>
                                <item
                                    v-show="!loading && !showJourneys"
                                    title="Where do you need support?"
                                    subtitle="Please select one or more"
                                    :items="categories"
                                    itemLabelKey="name"
                                    type="category"
                                />
                            </v-col>
                        </v-row>
                        <v-row center>
                            <v-col>
                                <v-btn role="button" aria-label="next" color="success" @click="selectCategories"
                                    >Next
                                    <v-icon>mdi-arrow-right-bold-circle</v-icon></v-btn
                                >
                            </v-col>
                        </v-row>
                    </v-form>

                    <v-form role="form" aria-label="Your journey" ref="journeys" v-show="!loading && showJourneys">
                        <v-row>
                            <v-col>
                                <item
                                    v-show="!loading && showJourneys"
                                    title="Where do you need support?"
                                    subtitle="Please select one or more"
                                    :items="possibleJourneys"
                                    itemLabelKey="label"
                                    type="journey"
                                />
                            </v-col>
                        </v-row>
                        <v-row center>
                            <v-col>
                                <v-btn role="button" aria-label="back" @click="selectCategories(false)">
                                    <v-icon left>mdi-arrow-left-bold-circle</v-icon>Back
                                </v-btn>
                                <v-btn role="button" aria-label="next" color="success" @click="beginAssessment"
                                    >Next
                                    <v-icon right>mdi-arrow-right-bold-circle</v-icon>
                                </v-btn>
                            </v-col>
                        </v-row>
                    </v-form>
                </v-container>
            </v-container>
        </v-sheet>
    </div>
</template>

<script>
import landing from "@/js/landing.js";
import Item from "@/components/Item.vue";

export default {
    components: {
        Item,
    },
    name: "Selection",
    created() {
        fetch(this.endpoint + "/journeys")
            .then((x) => x.json())
            .then((x) => {
                this.journeys = x;
                let uniqueParents = Array.from(
                    new Set(
                        x.map((journey) => {
                            return journey.parent;
                        })
                    )
                );
                this.categories = uniqueParents.map((parent) => {
                    return { name: parent, selected: false };
                });
                this.loading = false;
            });
    },
    computed: {
        showJourneys() {
            return this.categoriesSelected || this.categories.length <= 1;
        },
        selectedCats() {
            return this.categories.filter((x) => x.selected).map((x) => x.name);
        },
        possibleJourneys() {
            if (this.categories.length <= 1 || this.selectedCats.length === 0)
                return this.journeys;

            return this.journeys.filter(
                (x) => this.selectedCats.indexOf(x.parent) >= 0
            );
        },
        selectedJourneys() {
            if (this.possibleJourneys.length <= 1) return this.possibleJourneys;

            return this.possibleJourneys
                .filter((x) => x.selected)
                .map((x) => x.id);
        },
    },
    methods: {
        beginAssessment() {
            if (!this.$refs.journeys.validate()) {
                return false;
            }
            this.$router.push({
                name: "Assessment",
                params: { journeys: this.selectedJourneys },
            });
        },
        selectCategories(selected = true) {
            if (selected && !this.$refs.categories.validate()) {
                return false;
            }
            this.categoriesSelected = selected;
        },
    },
    data() {
        return {
            selc: [],
            selj: [],
            primaryColour: landing.get(),
            loading: true,
            categoriesSelected: false,
            endpoint: process.env.VUE_APP_API_ENDPOINT,
            categories: [],
            categories2: [],
            journeys: [],
        };
    },
};
</script>
