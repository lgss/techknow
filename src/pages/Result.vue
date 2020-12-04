<template>
    <v-container>
        <div v-if="loading">
            <v-skeleton-loader type="card" v-for="n in 5" :key="n" />
        </div>
        
        <div v-else>
            <v-banner single-line elevation="10" class="mb-10" v-for="banner in banners" :key="banner.id">
                <v-avatar color="primary" slot="icon">
                    <v-icon color="white">
                        {{banner.icon}}
                    </v-icon>
                </v-avatar>
                <div v-html="banner.content" />
                <template v-slot:actions="{dismiss}">
                    <v-btn color="primary" @click="dismiss" text>
                        dismiss
                    </v-btn>
                </template>          
            </v-banner>
            <div id="no_results" v-if="filteredList.length === 0">
                <div ref="heading" role="heading" aria-level="3" class="text-h4 mb-2" v-text="noResults.title" tabindex="0"></div>
                <v-col v-html="noResults.content"></v-col>
            </div>

            <v-container v-else id="container-results">
                <v-row v-for="category in categorisedList" :key="category.category">

                    <v-container>
                        <v-row class="align-center" >
                            <v-col class="text-left">
                                <div ref="heading" role="heading" aria-level="3" class="text-h4 mb-2" v-text="category.category" tabindex="0"></div>
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
            <v-container>
                <v-btn role="button" id="btn-restart-assessment" @click="startAgain">Start again</v-btn>
            </v-container>
        </div>
    </v-container>
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
            fetch(this.endpoint + "/banners")
                .then((bannerResponse) => bannerResponse.json())
                .then((bannerObject) => {
                    this.banners = bannerObject;
                }),
        ]).then(() => {
            this.loading = false;
            this.doFocus();
        });
    },
    props: ["responses"],
    methods: {
        startAgain() {
            this.$dialog
                .display(
                    "Start again",
                    "The resources currently shown will be lost. You will need to complete the assessment again from the beginning. Are you sure you want to start again?",
                    [{text:'Yes', color:''}, {text:'No', color:''}]
                )
                .then((result) => {
                    if (result === 0) this.$router.push({ name: "Select" });
                });
        },
        doFocus(){
            window.scrollTo(0,0);
            this.$nextTick(()=> {
                if(this.filteredList.length === 0) {
                    this.$refs[`heading`].focus()
                } else {
                    this.$refs[`heading`][0].focus()
                }
            })
        }
    },
    computed: {
        noResults() {
            return this.$store.state.pageContent.filter(x=>x.id=="CONTENT_POSITIVE")[0]
        },
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
            banners: [],
            loading: true,
            resources: [],
            endpoint: process.env.VUE_APP_API_ENDPOINT,
        };
    },
};
</script>
