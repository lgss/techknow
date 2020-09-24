<template>
  <div class="stimulus">
    <v-label ref="label" role="heading" aria-level="3" class="text-h3 mb-2" v-if="label">{{label}}</v-label>
    <div v-html="content"></div>
  </div>
</template>

<script>
  export default {
    name: 'Stimulus',
    props: ['content', 'label', 'name','align'],
    data() {
        return {}
    },
    methods :{
        focus() {
			this.$refs.label.focus()
        },
    }
  }
</script>

<style>
  .stimulus {
    text-align: left
  }
</style>