<template>
  <v-container fluid>
    <label>{{label}}</label>
    <v-radio-group v-model="value">
      <v-radio v-for="item in options" :label="item" value="False"></v-radio>
    </v-radio-group>
  </v-container>
</template>

<script>
  export default {
    data() {
        return {
            value: ''
        }
    },
    name: 'SingleChoiceInput',
    props: ['label', 'name', 'options']
  }
</script>