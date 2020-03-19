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
      :rules="[value => value.length > 0 || 'Please select at least one response']"
    ></v-checkbox>
  </v-container>
</template>

<script>
  export default {
    name: 'JourneySelector',
    props: ['label', 'name', 'choices'],
    data() {
        return {
            value: []
        }
    },
    methods: {
      onChange: function() {
        this.$emit('journeyResponded', this.value)
      }
    }
  }
</script>