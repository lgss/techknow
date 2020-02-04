<template>
  <v-container fluid>
    <label>{{label}}</label>
    <v-radio-group v-model="selectedOption" @change="onChange">
      <v-radio v-for="option in options" :key="option.value" :label="option.value" :value="option"></v-radio>
    </v-radio-group>
  </v-container>
</template>

<script>
  export default {
    name: 'SingleChoiceInput',
    props: ['label', 'name', 'options'],
    data() {
        return {
            selectedOption: {}
        }
    },
    methods: {
      onChange: function() {
        this.$emit('answered', [this.selectedOption])
      }
    }
  }
</script>