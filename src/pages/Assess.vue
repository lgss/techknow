<template>
  <div>
    <v-card>
      <v-stepper v-model="pageIdx" style="box-shadow: none">
        <v-progress-linear tile="true" color="primary" :value='percentDone'/>
        <v-stepper-items>
          <v-stepper-content 
            v-for="(page, idx) in displayPages"
            :key="page.id"
            :step="idx + 1"
            class="assessment-page"
            :class="isCurrentPage(idx)">
            <v-form :ref="'page' + (idx + 1)">
              <h2>{{page.title}}</h2>
              <v-row v-for="(field, index) in page.items" :key="index" class="assessment-item">
                <v-col>
                  <component @responded='(selection)=>responded(selection,field.name)' :is="field.fieldType" v-bind="field"/>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-btn :disabled="pageIdx <= 1" name='btn-back' @click.native="prior">Back</v-btn>
                  <v-btn v-if='finished' color="success" name='btn-finish' :to="{name:'Result', params: {responses}}">Finish</v-btn>
                  <v-btn v-else color="success" name="btn-next" @click.native="next">Next</v-btn>
                </v-col>
              </v-row>
            </v-form>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-card>
  </div>
</template>

<script>
import SmallTextInput from '../components/controls/SmallTextInput.vue'
import SingleChoiceInput from '../components/controls/SingleChoiceInput.vue'
import MultipleChoiceInput from '../components/controls/MultipleChoiceInput.vue'
import BooleanInput from '../components/controls/BooleanInput.vue'
import Stimulus from '../components/controls/Stimulus.vue'

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
    computed: {
      percentDone() {
        return Math.round(this.pageIdx/this.fields.pages.length*100)
      },
      finished() {
        return this.pageIdx >= this.fields.pages.length;
      },
      
      displayPages() {
        // Arguably, this should filter the pages but it'd make progress tracking harder
        let self = this;

        return this.fields.pages.map(function(pg) { 
            let newPg = Object.assign({}, pg)

            newPg.items = pg.items.filter(x => 
              !self.intersects(x.excludeTags, self.tags)
              && (self.intersects(x.includeTags, self.tags)
              || (x.includeTags || []).length === 0))
              
            return newPg
          }
        )
      }
    },
    methods: {
      next() {
        let page_valid = this.validatePage()
        if (!page_valid) {
          return false
        }
        this.movePage(true)
      },
      prior() {
        this.movePage(false)
      },
      pageEmpty() {
        return this.displayPages[this.pageIdx - 1].items.length < 1
      },
      movePage(forwards) {
        if (forwards)
          this.pageIdx++
        else 
          this.pageIdx--

        if (this.pageEmpty())
          this.movePage(forwards)
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

        this.tags = this.responses.flatMap(x => x.choices).flatMap(x => x.tags)
      },
      isCurrentPage(idx) {
        return (idx + 1) == this.pageIdx ? `current` : null
      },
      intersects(one, two) {
        return one && two && (one.find(element => two.includes(element)) !== undefined)
      },
      getResponseTags(responses) {
        return responses.flatMap(x => x.choices).flatMap(x => x.tags)
      },
      validatePage(page) {
        //find current page if null page argument
        page = page || this.displayPages[this.pageIdx-1]
        let page_valid = page.items.every(this.validateItem)
        return page_valid
      },
      validateItem(item) {
        item.valid = this.responses.some(response => {
          return response.name === item.name && response.choices.length
        })
        return item.valid
      }
    },
    props: ["fields"],
    data() {
      return {
        pageIdx: 1,
        responses: [],
        tags: [], // this is here to allow quick assessment mutations but I suspect that you
                  // could achieve the same by watching `responses`
        dialog: {},
        showDialog: false
      }
    }
}
</script>