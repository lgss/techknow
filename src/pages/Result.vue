<template>
  <div>
    <v-btn id="btn-restart-assessment" @click="startAgain">Start again</v-btn>
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
const resources =  require('../../static/resource.json');

export default {
    name: 'Result',
    components: {},
    props: ["responses"],
    methods: {
      startAgain() {
        this.$dialog('Start again', 'The resources currently shown will be lost. You will need to complete the assessment again from the beginning. Are you sure you want to start again?', ['Yes', 'No'])
          .then(result => {if (result === 0) 
              this.$router.push({ name: 'Assessment'})})
      },
      getResponseTags(responses) {
        return responses.flatMap(x => x.choices).flatMap(x => x.tags)
      }
    },
    computed: {
      filteredList: {
        get () {
          return this.resources.resources
            .filter(resource => resource.includeTags
              .some(IncludeTag => this.getResponseTags(this.responses)
                .some(responseTag => responseTag == IncludeTag)
              )
            )
            .filter(resource => !resource.excludeTags
              .some(ExcludeTag => this.getResponseTags(this.responses)
                .some(responseTag => responseTag == ExcludeTag)
              )
            )
        }
      }
    },
    data(){
        return {
          resources
        }
    }
}
</script>