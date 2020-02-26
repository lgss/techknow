<template>
    <v-card>
      <v-stepper v-model="pageIdx" style="box-shadow: none">
        <v-progress-linear tile="true" color="primary" :active='true' :value='percentDone'/>
        
        <v-stepper-items>
          <v-stepper-content 
            v-for="(page, idx) in fields.pages"
            :key="page.id"
            :step="idx + 1"
            class="assessment-page"
            :class="isCurrentPage(idx)">
            <v-form :ref="'page' + (idx + 1)">
              <h2>{{page.title}}</h2>
              <v-row v-for="(field, index) in page.items" :key="index" class="assessment-item" :class="field.display">
                <v-col>
                  <component @responded='(selection)=>responded(selection,field.name)' :is="field.fieldType" v-bind="field"/>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-btn :disabled="pageIdx <= 1" name='btn-back' @click.native="prior">Back</v-btn>
                  <v-btn v-if='finished' color="success" name='btn-finish' to="/result">Finish</v-btn>
                  <v-btn v-else color="success" name="btn-next" @click.native="next">Next</v-btn>
                </v-col>
              </v-row>
            </v-form>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-card>
</template>

<script>
import SmallTextInput from '../components/controls/SmallTextInput.vue'
import SingleChoiceInput from '../components/controls/SingleChoiceInput.vue'
import MultipleChoiceInput from '../components/controls/MultipleChoiceInput.vue'
import BooleanInput from '../components/controls/BooleanInput.vue'

export default {
    name: "Assess",
    components: {
      'small-text-input': SmallTextInput,
      'single-choice-input': SingleChoiceInput,
      'multiple-choice-input': MultipleChoiceInput,
      'boolean-input': BooleanInput
    },
    computed: {
      percentDone() {
        return Math.round(this.pageIdx/this.fields.pages.length*100)
      },
      finished() {
        return this.pageIdx >= this.fields.pages.length;
      }
    },
    methods: {
      next() {
        this.getPageIdX("next")
      },
      prior() {
        this.getPageIdX("prior")
      },
      getPageIdX(direction) {
        let exit = false
        while(exit == false) {
          //Check for direction
          if(direction == "next") { 
            this.pageIdx ++
          } else {
            this.pageIdx --
          }
          // check if the page has visible items
          this.fields.pages[this.pageIdx-1].items.forEach(item => {
            if (item["display"] == "visible") {
              exit = true // if a page has a visible item then exit the loop
            }
            if (direction == "next" && this.pageIdx == this.fields.pages.length || direction == "prior" && this.pageIdx == 0 ) {
              exit = true // if the user is on the last item then exit the loop
            }
          })
        }
      },
      responded(selection,name) {
        var response = {
          name: name,
          choices: selection
        }
        var currentResponseIndex = this.responses.findIndex(response => (response.name === name))
        if (currentResponseIndex >= 0) {
          this.responses[currentResponseIndex] = response
        } else {
          this.responses.push(response)
        }
        // evaluates which fields should be visible when a user updates their responses
        this.isVisible()
      },
      isCurrentPage(idx) {
        return (idx + 1) == this.pageIdx ? `current` : null
      },
      isVisible() {      
        let responseTags = this.getResponseTags(this.responses)
        this.fields.pages.forEach(page => {
            page.items.forEach(item => {
              if (this.intersection(item.excludeTags,responseTags)) { 
                this.$set(item,'display', "hidden")
                //item["display"] = "hidden" // if an exclude tag matchs a response tag then it will be hidden. 
              }
              else if (item.includeTags.length == 0) { 
                this.$set(item,'display', "visible")
                //item["display"] = "visible" // if no include tags are provide then the item will display as default
              }
              else if (this.intersection(item.includeTags,responseTags)) {
                this.$set(item,'display', "visible")
                //item["display"] = "visible" // if an include tag matchs a response tag then it will be displayed
              }
              else {
                this.$set(item,'display', "hidden")
                //item["display"] = "hidden" // if the include tags are not in the users responses then the item will be hidden
              }
            })
        });
      this.$forceUpdate() // this is being used to force refresh the dom when changes are made to the same page. 
      },
      intersection(fieldTags,responseTags) {
        // checks if the two arrays have any elements that equal each other
        return responseTags.filter(element => fieldTags.includes(element)).length > 0
      },
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
    mounted() {
      this.isVisible()
    },
    props: ["fields", "responses"],
    data() {
      return {
        pageIdx: 1
      }
    }
}
</script>
<style>
.hidden {
  visibility: hidden;
  height:0;
}
</style>