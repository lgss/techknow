<template>
    <v-card>
      <v-stepper v-model="pageIdx" style="box-shadow: none">
        <v-progress-linear tile="true" color="primary" :active='true' :value='percentDone'/>
        
        <span v-if="fields.pages.length < 20">Page {{pageIdx}}/{{fields.pages.length}}</span>
        <span v-else>{{percentDone}}%</span>
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
                  <component @answered='(result)=>answered(result,field.name)' :is="field.fieldType" v-bind="field" />
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
      answered(result,name) {
        var answer = {
          name: name,
          options: result
        }
        var currentAnswerIndex = this.answers.findIndex(answer => (answer.name === name))
        if (currentAnswerIndex >= 0) {
          this.answers[currentAnswerIndex] = answer
        } else {
          this.answers.push(answer)
        }
      },
      isCurrentPage(idx) {
        return (idx + 1) == this.pageIdx ? `current` : null
      }
    },
    props: ["fields", "answers"],
    data() {
      return {
        pageIdx: 1
      }
    }
}
</script>