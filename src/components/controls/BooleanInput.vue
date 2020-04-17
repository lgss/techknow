<template>
  <v-container>
    <v-switch v-model="value" :label="label" :rules="rules"></v-switch>
  </v-container>
</template>

<script>
  export default {
    data() { 
        return {
            value: false,
            rules: this.isMandatory ? [choice => choice !== undefined || "Please select this option"] : []
        }
    },
    name: 'SmallTextInput',
    props: ['label', 'name', 'isMandatory']
  }
</script>