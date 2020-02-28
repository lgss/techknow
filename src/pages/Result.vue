<template>
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
              </div>
                            <div> 
                <v-chip v-for="eTag in resource.excludeTags" :key="eTag" class="ma-2" color="red" text-color="white">
                  {{ eTag }}
                </v-chip>
              </div>
            </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
const resources =  require('../../static/resource.json');

export default {
    name: 'Result',
    components: {},
    props: ["responses"],
    methods: {
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

<style>

</style>