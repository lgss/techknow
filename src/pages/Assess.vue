<template>
  <div>
    <v-card>
      <v-stepper v-model="pageIdx" style="box-shadow: none">
        <v-progress-linear tile="true" color="primary" :value='percentDone' :indeterminate="loading" />
        <div v-if="loading">
          <br/>
          <h2>Loading...</h2>
          <br/>
        </div>
        <v-stepper-items>
          <v-stepper-content 
            v-for="(page, idx) in displayPages"
            :key="page.id"
            :step="idx + 1"
            class="assessment-page"
            :class="isCurrentPage(idx)">
            <v-form ref="page" lazy-validation>
              <h2>{{page.title}}</h2>
              <v-row v-for="(field, index) in page.items" :key="index" class="assessment-item">
                <v-col>
                  <component @responded='(selection)=>responded(selection,field.name)' :is="field.fieldType" v-bind="field"/>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-btn :disabled="pageIdx <= 1" name='btn-back' @click.native="prior">Back</v-btn>
                  <v-btn v-if='finished' color="success" name='btn-finish' @click="finish">Finish</v-btn>
                  <v-btn v-else color="success" name="btn-next" @click.native="next">Next</v-btn>
                </v-col>
              </v-row>
            </v-form>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-card>    
    <v-dialog v-model="showDialog" :fullscreen="dialog.fullscreen">
      <v-card>
        <v-container>
          <v-row>
            <v-col>
              <h1 id="dialog-title" v-html="dialog.title"></h1>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <span v-html="dialog.content"></span>
            </v-col>
          </v-row>
          <v-row justify="center">
            <v-btn @click="showDialog = false">Back</v-btn>
          </v-row>
        </v-container>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import SmallTextInput from '../components/controls/SmallTextInput.vue'
import SingleChoiceInput from '../components/controls/SingleChoiceInput.vue'
import MultipleChoiceInput from '../components/controls/MultipleChoiceInput.vue'
import BooleanInput from '../components/controls/BooleanInput.vue'
import Stimulus from '../components/controls/Stimulus.vue'
import utils from '@/js/assess-utils.js'

export default {
    name: "Assess",
    self: this,
    components: {
      'small-text-input': SmallTextInput,
      'single-choice-input': SingleChoiceInput,
      'multiple-choice-input': MultipleChoiceInput,
      'boolean-input': BooleanInput,
      'stimulus': Stimulus
    },
    created() {
      fetch('https://nngfac1fjl.execute-api.eu-west-2.amazonaws.com/dev' + '/journeys/')
        .then(x => x.json())
        .then(x => {this.journeys = x})
        .finally(() => {
          // Manipulate journeys to be a choice list
          let choices = []
          this.journeys.forEach(j => {
            let choice = {
              "value": j.label,
              "doc": JSON.parse(j.doc)
            }
            choices.push(choice)
          });
          // Create a false page to display list of journeys
          this.fields = 
          {
            "pages": [
              {
                "title": "How can we help you today?",
                "items": [
                  {
                    "fieldType":"multiple-choice-input",
                    "name":"journey-selection",
                    "label":"Select items that you need help with",
                    "choices": choices
                  }
                ]
              }
            ]
          }
          this.loading = false
          this.pageIdx = 1
        })
    },
    computed: {
      percentDone() {
        return Math.round(this.pageIdx/this.displayPages.length*100)
      },
      finished() {
        return this.pageIdx >= this.displayPages.length && this.start;
      },
      
      displayPages() {
        // Arguably, this should filter the pages but it'd make progress tracking harder
        let self = this;

        if (!this.fields.pages)
          return [{}]

        return this.fields.pages.map(function(pg) { 
            let newPg = Object.assign({}, pg)

            newPg.items = pg.items.filter(x => 
              !utils.intersects(x.excludeTags, self.tags)
              && (utils.intersects(x.includeTags, self.tags)
              || (x.includeTags || []).length === 0))
              
            return newPg
          }
        )
      }
    },
    methods: {
      next() {
        if(this.start) {
          // Validate that items on the page contain responses
          let page_valid = this.$refs.page[this.pageIdx - 1].validate() 
          if (!page_valid) {
            return
          }
          // checks if a dialog needs to be displayed to the user
          if (this.proceedDialog()) {
            return
          }
          // navigates to the next page
          this.movePage(true)
        } else {
          this.fields = this.concatFields
          this.start = true;
        }
      },
      prior() {
        this.movePage(false)
      },
      pageEmpty() {
        return this.displayPages[this.pageIdx - 1].items.length < 1
      },
      movePage(forwards) {
        if (this.proceedDialog()) 
          return

        if (forwards)
          this.pageIdx++
        else 
          this.pageIdx--

        if (this.pageEmpty())
          this.movePage(forwards)
      },
      responded(selection,name) {
        if(name == "journey-selection") {
          this.concatFields = {
            "pages": selection.flatMap(x => x.doc.pages)
          }
        } else {
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

          this.tags = this.responses.flatMap(x => x.choices).flatMap(x => x.tags)
        }
      },
      isCurrentPage(idx) {
        return (idx + 1) == this.pageIdx ? `current` : null
      },
      finish() {
        if(this.proceedDialog()) {
          return
        }
        this.$router.push({name:'Result', params: {responses: this.responses}})
      },
      proceedDialog() {
        const choice = this.responses.flatMap(response => (response.choices)).find(choice => "dialog" in choice)

        if (choice && "dialog" in choice) {
          this.dialog = choice.dialog
          this.showDialog = true
          return true;
        }
        
        return false;
      }
    },
    data() {
      return {
        loading: true,
        journeys:[],
        start: false,
        concatFields: {},
        fields: {},
        pageIdx: 0,
        responses: [],
        tags: [], // this is here to allow quick assessment mutations but I suspect that you
                  // could achieve the same by watching `responses`
        dialog: {},
        showDialog: false
      }
    }
}
</script>