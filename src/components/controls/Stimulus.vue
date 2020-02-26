<template>
  <v-container fluid>
        <v-col :align='this.align'>
            <v-row>
                <v-label>{{label}}</v-label>
            </v-row>
            <v-row>
                <div v-html="content"></div>
            </v-row>
      </v-col>
  </v-container>
</template>

<script>
  export default {
    name: 'Stimulus',
    props: ['content', 'label', 'name','align'],
    data() {
        return {}
    }
  }
</script>