<template>
  <v-container fluid>
    <div class="text-left">
      <h2>{{label}}</h2>
      <h3>Please select one or more</h3>
    </div>
    <v-item-group multiple v-model="sel" @change="onChange" :rules="rules" :class="name">
      <v-row dense>
          <v-col v-for="choice in choices" :key="choice.value" :value="choice" cols="12">
              <choice :value="choice" :index="choice" :label="choice.value"/>
          </v-col>
      </v-row>
    </v-item-group>
  </v-container>

</template>

<script>
  import Choice from '@/components/controls/Choice.vue'
  export default {
    name: 'MultipleChoiceInput',
    props: ['label', 'name', 'choices', 'isMandatory'],
    components: {
      Choice,
    },
    data() {
        return {
            sel: [],
            rules: this.isMandatory ? [value => value.length > 0 || 'Please select at least one response'] : []
        }
    },
    methods: {
      onChange: function() {
        console.log(this.sel)
        this.$emit('responded', this.sel)
      }
    }
  }
</script>