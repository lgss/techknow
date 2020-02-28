<template>
  <div>
    <div class="button-container">
      <v-btn id="btn-restart-assessment" @click="restartDialog = true">Start Again</v-btn>
      <v-dialog v-model="restartDialog" max-width="600px">
        <v-card>
          <v-card-title>Are you sure?</v-card-title>
          <v-card-text>The resources currently shown will be lost. You will need to complete the assessment again from the beginning.</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn id="btn-restart-confirm" @click="restart">Continue</v-btn>
            <v-btn id="btn-restart-cancel"  @click="restartDialog = false">Cancel</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
    <v-container id="container-results">
      <v-row v-for="resource in filteredList " :key="resource.name">
        <v-col>
            <v-card class="mx-auto" max-width="344">
              <v-card-text>
                <p class="display-1 text--primary"> {{ resource.name }}</p>
                <div class="text--primary"> 
                  <span v-html="resource.content"></span>
                </div>
                <div> 
                  <v-chip v-for="tag in resource.tags" :key="tag" class="ma-2">
                    {{ tag }}
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
export default {
    name: 'Result',
    components: {},
    props: ["results", "answers"],
    methods: {
      getAnswerTags(answers) {
        let tags = []
        answers.forEach(answer => {
            answer.options.forEach( option => {
              option.tags.forEach(tag => {
                tags.push(tag)
              })
            })
        })
        return tags
      },
      restart() {
          this.$router.push({ path: '/assess'})
      }
    },
    computed: {
      filteredList: {
        get () {
          return this.results.resources.filter(resource => resource.tags.some(resourceTag => this.getAnswerTags(this.answers).some(answerTag => answerTag == resourceTag)))
        }
      }
    },
    data(){
        return {
          restartDialog: false
        }
    }
}
</script>

<style>
  .button-container {
    text-align: left; 
  }
</style>