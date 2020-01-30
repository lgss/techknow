<template>
  <v-container fluid>
    <label>{{label}}</label>
    <v-radio-group v-model="value">
      <v-radio v-for="item in options" :key="item" :label="item" :value="item"></v-radio>
    </v-radio-group>
  </v-container>
</template>

<script>
  export default {
    name: 'SingleChoiceInput',
    props: ['label', 'name', 'options'],
    data() {
        return {
            value: ''
        }
    }
  }
</script>