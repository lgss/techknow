<template>
    <v-card>
      <v-stepper v-model="pageIdx" style="box-shadow: none">
        <v-progress-linear tile="true" color="primary" :active='true' :value='percentDone'/>
        
        <span v-if="fields.pages.length < 20">Page {{pageIdx}}/{{fields.pages.length}}</span>
        <span v-else>{{percentDone}}%</span>
        <v-stepper-items>
          <v-stepper-content
            v-for="(page, idx) in fields.pages"
            :key="pageIdx.id"
            :step="idx + 1">
            <v-form :ref="'page' + (idx + 1)">
              <h2>{{page.title}}</h2>
              <v-row v-for="(field, index) in page.items" :key="index" >
                <v-col>
                  <component :is="field.fieldType" v-bind="field" />
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-btn :disabled="pageIdx <= 1" @click.native="prior">Back</v-btn>
                  <v-btn color="success" @click.native="next">Next</v-btn>
                </v-col>
              </v-row>
            </v-form>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-card>
</template>

<script>
import BooleanInputVue from "../components/controls/BooleanInput.vue"


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
      }
    },
    methods: {
      next() {
        if (this.pageIdx < this.fields.pages.length ){//&& this.$refs['page' + this.pageIdx].validate()) {
          this.pageIdx++
        } else {

        }
      },
      prior() {
          this.pageIdx--
      }
    },
    props: ["fields"],
    data() {
      return {
        pageIdx: 1
      }
    }
}
</script>