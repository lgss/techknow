<template>
  <v-container fluid>
      <v-div>{{content}}</v-div>
  </v-container>
</template>

<script>
  export default {
    name: 'Stimulus',
    props: ['content', 'label', 'name'],
    data() {
        return {}
    }
  }
</script>