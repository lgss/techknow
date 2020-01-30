<template>
  <v-container fluid>
    <label>{{label}}</label>
      <v-checkbox v-for="item in options" v-model="value" :key="item" :label="item" :value="item"></v-checkbox>
      <p> selected: {{ value }}</p>
  </v-container>
</template>

<script>
  export default {
    name: 'MultipleChoiceInput',
    props: ['label', 'name', 'options'],
    data() {
        return {
            value: []
        }
    }
  }
</script>