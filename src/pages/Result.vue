<template>
    <div>
        <div v-if="loading">
            <v-skeleton-loader type="card" v-for="n in 5" :key="n" />
        </div>
        
        <div v-else>
            <div id="no_results" v-if="filteredList.length === 0">
                <div role="heading" aria-level="3" class="text-h3 mb-2" v-text="noResults.title" tabindex="0"></div>
                <v-col v-html="noResults.content"></v-col>
                <v-btn role="button" id="btn-restart-assessment" @click="startAgain">Start again</v-btn>
            </div>

            <v-container v-else id="container-results">
                <v-row v-for="category in categorisedList" :key="category.category">

                    <v-container>
                        <v-row class="align-center" >
                            <v-col class="text-left">
                                <div role="heading" aria-level="3" class="text-h3 mb-2" v-text="category.category" tabindex="0"></div>
                            </v-col>
                        </v-row>
                    </v-container>

                    <v-container>
                        <v-row>
                            <v-col cols="12" md="6" v-for="resource in category.resources" :key="resource.name">
                                <resource v-bind="resource" />
                            </v-col>
                        </v-row>
                    </v-container>

                </v-row>
            </v-container>

        </div>
    </div>
</template>

<script>
import utils from "@/js/assess-utils.js";
import resource from "@/components/Resource.vue";

export default {
    name: "Result",
    self: this,
    components: { resource },
    created() {
        Promise.all([
            fetch(this.endpoint + "/resources")
                .then((x) => x.json())
                .then((x) => {
                    this.resources = x;
                }),
            fetch(this.endpoint + "/config/positive-outcome")
                .then((x) => x.json())
                .then((x) => (this.noResults = x)),
        ]).then(() => {
            window.scrollTo(0,0);
            this.loading = false;
        });
    },
    props: ["responses"],
    methods: {
        startAgain() {
            this.$dialog
                .display(
                    "Start again",
                    "The resources currently shown will be lost. You will need to complete the assessment again from the beginning. Are you sure you want to start again?",
                    ["Yes", "No"]
                )
                .then((result) => {
                    if (result === 0) this.$router.push({ name: "Select" });
                });
        },
    },
    computed: {
        filteredList() {
            if (this.loading == true) {
                return [];
            }
            let responseTags = utils.getResponseTags(this.responses);
            try {
                return this.resources.filter(
                    (resource) =>
                        utils.intersects(
                            resource.doc.includeTags,
                            responseTags
                        ) &&
                        !utils.intersects(
                            resource.doc.excludeTags,
                            responseTags
                        )
                );
            } catch (error) {
                console.log(error);
                return [];
            }
        },
        categorisedList() {
            if (!this.filteredList.length) return [];
            return this.filteredList
                .flatMap((r) => r.doc.categories)
                .filter((cat, i, a) => a.indexOf(cat) == i)
                .map((cat) => ({
                    category: cat,
                    resources: this.filteredList.filter((r) =>
                        r.doc.categories.some((c) => c == cat)
                    ),
                }));
        },
    },
    data() {
        return {
            loading: true,
            resources: [],
            noResults: {},
            endpoint: process.env.VUE_APP_API_ENDPOINT,
        };
    },
};
</script>
