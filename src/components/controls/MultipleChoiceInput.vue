<template>
  <v-container fluid>
    <label>{{label}}</label>
    <v-checkbox 
      v-for="choice in choices"
      v-model="value"
      :key="choice.value"
      :label="choice.value"
      :value="choice"
      hide-details
      @change="onChange"
    ></v-checkbox>
  </v-container>
</template>

<script>
  export default {
    name: 'MultipleChoiceInput',
    props: ['label', 'name', 'choices'],
    data() {
        return {
            value: []
        }
    },
    methods: {
      onChange: function() {
        this.$emit('responded', this.value)
      }
    }
  }
</script>