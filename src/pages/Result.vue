<template>
  <v-container id="container-results">
    <v-row v-for="resource in results.resources.filter(resource => checkTags(answers, resource.tags))" :key="resource.name">
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
</template>

<script>
export default {
    name: 'Result',
    components: {},
    props: ["results", "answers"],
    methods: {
      checkTags(answers, tags) {
        return tags.some(resourceTag => this.getAnswerTags(answers).some(answerTag => answerTag == resourceTag))
      },
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
      }
    },
    data(){
        return {}
    }
}
</script>

<style>

</style>