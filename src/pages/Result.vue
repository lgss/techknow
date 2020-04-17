<template>
  <div>
    <div v-if="loading">
      <br/>
      <h2>Loading...</h2>
      <br/>
    </div>
    <div v-else-if="filteredList.length === 0">
      <h1>No results header</h1>
      <p>When no results are returned content should be displayed here like: Lorem ipsum dolor sit amet,
         consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
         Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
         Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      <v-btn id="btn-restart-assessment" @click="startAgain">Start again</v-btn>
    </div>
    <v-container v-else id="container-results">
      <v-row v-for="resource in filteredList " :key="resource.name">
        <v-col>
            <v-card class="mx-auto resource">
              <v-card-text>
                <p class="display-1 text--primary"> {{ resource.name }}</p>
                <div class="text--primary"> 
                  <span v-html="resource.content"></span>
                </div>
                <div> 
                  <v-chip v-for="iTag in resource.includeTags" :key="iTag" class="ma-2" color="green" text-color="white">
                    {{ iTag }}
                  </v-chip>
                  <v-chip v-for="eTag in resource.excludeTags" :key="eTag" class="ma-2" color="red" text-color="white">
                    {{ eTag }}
                  </v-chip>
                </div>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
</template>

<script>
import utils from '@/js/assess-utils.js'

export default {
    name: 'Result',
    self: this,
    components: {},
    created() {
      fetch('https://1dds21470e.execute-api.eu-west-2.amazonaws.com/dev/resources')
        .then(x =>x.json())
        .then(x => {this.resources = x})
        .catch((err)=>{})
        .finally(() => {
          this.loading = false
        })
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
            utils.intersects(resource.includeTags, responseTags) && 
            !utils.intersects(resource.excludeTags, responseTags))
        } catch (error) {
          return []          
        }
      }
    },
    data(){
        return {
          loading: true,
          resources: {}
        }
    }
}
</script>

<style>
.v-card.resource {
  max-width: 600;
}
</style>
