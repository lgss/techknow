<template>
  <v-container fluid>
    <label class="item-stimulus">{{label}}</label>
    <v-checkbox 
      v-for="choice in choices"
      v-model="value"
      :key="choice.value"
      :label="choice.value"
      :value="choice"
      hide-details
      @change="onChange"
      :rules="rules"
    ></v-checkbox>
  </v-container>
</template>

<script>
  export default {
    name: 'MultipleChoiceInput',
    props: ['label', 'name', 'choices', 'isMandatory'],
    data() {
        return {
            value: [],
            rules: this.isMandatory ? [value => value.length > 0 || 'Please select at least one response'] : []
        }
    },
    methods: {
      onChange: function() {
        this.$emit('responded', this.value)
      }
    }
  }
</script>