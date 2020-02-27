<template>
  <div>
    <div class="button-container">
      <v-btn id="btn-restart-assessment" @click.native="restart">Start Again</v-btn>
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
        if(confirm("Are you sure you want to start again? The current results will be lost")){
          this.$router.push({ path: '/assess'})
        }
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
        return {}
    }
}
</script>

<style>
  .button-container {
    text-align: left; 
  }
</style>