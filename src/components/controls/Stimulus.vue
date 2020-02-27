<template>
  <div class="stimulus">
    <v-label v-if="label">{{label}}</v-label>
    <div v-html="content"></div>
  </div>
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

<style>
  .stimulus {
    text-align: left
  }
</style>