<template>
  <v-container fluid>
    <label>{{label}}</label>
    <v-radio-group v-model="selectedChoice" @change="onChange" :rules="rules" :class="name">
      <v-radio 
        v-for="choice in choices" 
        :key="choice.value" 
        :label="choice.value" 
        :value="choice"
      ></v-radio>
    </v-radio-group>
  </v-container>
</template>

<script>
  export default {
    name: 'SingleChoiceInput',
    props: ['label', 'name', 'choices', 'isMandatory'],
    data() {
        return {
            selectedChoice: {},
            rules: this.isMandatory ? [choice => choice.value !== undefined || 'Please select a response'] : []
        }
    },
    methods: {
      onChange: function() {
        this.$emit('responded', [this.selectedChoice])
      }
    }
  }
</script>