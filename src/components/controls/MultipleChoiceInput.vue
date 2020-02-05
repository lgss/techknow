<template>
  <v-container fluid>
    <label>{{label}}</label>
    <v-checkbox v-for="option in options" v-model="value" :key="option.value" :label="option.value" :value="option.value" hide-details></v-checkbox>
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