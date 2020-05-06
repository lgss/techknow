<template>
  <div>
    <div v-if="loading" >
      <v-skeleton-loader type="card" v-for="n in 5" :key="n"/>
    </div>
    <div v-else>
      <div v-if="filteredList.length === 0">
        <h1>{{ noResults.title }}</h1>
        <v-col v-html="noResults.content"></v-col>
        <v-btn id="btn-restart-assessment" @click="startAgain">Start again</v-btn>
      </div>
      <v-container v-else id="container-results">
        <v-row v-for="resource in filteredList " :key="resource.name">
          <v-col>
              <v-card class="mx-auto resource">
                <v-card-text>
                  <p class="display-1 text--primary"> {{ resource.doc.name }}</p>
                  <div class="text--primary"> 
                    <span v-html="resource.doc.content"></span>
                  </div>
                  <div> 
                    <v-chip v-for="iTag in resource.doc.includeTags" :key="iTag" class="ma-2" color="green" text-color="white">
                      {{ iTag }}
                    </v-chip>
                    <v-chip v-for="eTag in resource.doc.excludeTags" :key="eTag" class="ma-2" color="red" text-color="white">
                      {{ eTag }}
                    </v-chip>
                  </div>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </div>
  </div>
</template>

<script>
import utils from '@/js/assess-utils.js'

export default {
    name: 'Result',
    self: this,
    components: {},
    created() {
      Promise.all([
        fetch(this.endpoint + '/resources')
          .then(x =>x.json())
          .then(x => {this.resources = x}),
        fetch(this.endpoint + '/config/positive-outcome')
          .then(x=>x.json())
          .then(x=> this.noResults = x)]
      ).then(() => {this.loading = false})
    },
    props: ["responses"],
    methods: {
      startAgain() {
        this.$dialog.confirm('Start again', 'The resources currently shown will be lost. You will need to complete the assessment again from the beginning. Are you sure you want to start again?')
          .then(result => {if (result === 0) 
              this.$router.push({ name: 'Assessment'})})
      }
    },
    computed: {
      filteredList() {          
        if(this.loading == true) {
          return []
        }
        let responseTags = utils.getResponseTags(this.responses)
        try {
          return this.resources.filter(resource => 
            utils.intersects(resource.doc.includeTags, responseTags) && 
            !utils.intersects(resource.doc.excludeTags, responseTags))
        } catch (error) {
          console.log(error)
          return []          
        }
      }
    },
    data(){
        return {
          loading: true,
          resources: [],
          noResults: {},
          endpoint: process.env.VUE_APP_API_ENDPOINT
        }
    }
}
</script>

<style>
.v-card.resource {
  max-width: 600;
}
</style>
