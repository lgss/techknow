<template>
  <v-container fluid>
    <label class="item-stimulus">{{label}}</label>
    <v-radio-group v-model="selectedChoice" @change="onChange" :rules="[choice => choice.value !== undefined || 'Please select a response']" :class="name">
      <v-radio 
        v-for="choice in choices" 
        :key="choice.value" 
        :label="choice.value" 
        :value="choice"
      ></v-radio>
    </v-radio-group>
  </v-container>
</template>

<script>
  export default {
    name: 'SingleChoiceInput',
    props: ['label', 'name', 'choices'],
    data() {
        return {
            selectedChoice: {}
        }
    },
    methods: {
      onChange: function() {
        this.$emit('responded', [this.selectedChoice])
      }
    }
  }
</script>