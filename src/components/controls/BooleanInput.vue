<template>
  <v-container>
    <v-switch v-model="value" :label="label"></v-switch>
  </v-container>
</template>

<script>
  export default {
    data() { 
        return {
            value: false
        }
    },
    name: 'SmallTextInput',
    props: ['label', 'name']
  }
</script>