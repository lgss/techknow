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
              <v-row v-for="(field, index) in page.items" :key="index" class="assessment-item">
                <v-col>
                  <component @responded='(selection)=>responded(selection,field.name)' :is="field.fieldType" v-bind="field" />
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
        if (this.pageIdx < this.fields.pages.length && this.$refs['page' + this.pageIdx]) {
          this.pageIdx++
        } else {
          
          }
      },
      prior() {
        this.pageIdx--
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
      },
      isCurrentPage(idx) {
        return (idx + 1) == this.pageIdx ? `current` : null
      }
    },
    props: ["fields", "responses"],
    data() {
      return {
        pageIdx: 1
      }
    }
}
</script>