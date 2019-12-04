<template>
  <v-container fluid>
    <label>{{label}}</label>
    <v-checkbox v-for="item in options" :label="item" :value="item"></v-checkbox>
  </v-container>
</template>

<script>
  export default {
    name: 'MultipleChoiceInput',
    props: ['label', 'name', 'options']
  }
</script>