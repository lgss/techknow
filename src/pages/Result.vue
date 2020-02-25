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
    props: ["resources", "responses"],
    methods: {
      getResponseTags(responses) {
        let tags = []
        responses.forEach(response => {
            response.choices.forEach( choice => {
              choice.tags.forEach(tag => {
                tags.push(tag)
              })
            })
        })
        return tags
      }
    },
    computed: {
      filteredList: {
        get () {
          return this.resources.resources.filter(resource => resource.tags.some(resourceTag => this.getResponseTags(this.responses).some(responseTag => responseTag == resourceTag)))
        }
      }
    },
    data(){
        return {}
    }
}
</script>

<style>

</style>