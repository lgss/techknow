<template>
  <v-container>
    <v-text-field type="text"
          :label="label"
          :name="name"
          :placeholder="placeholder"
          :value="value"
          v-on:input="$emit('input', $event.target.value)">
    </v-text-field>
  </v-container>
</template>

<script>
  export default {
    name: 'SmallTextInput',
    props: ['placeholder', 'label', 'name', 'isMandatory'],
    data() {
        return {
            value: '',
            rules: this.isMandatory ? [value => value.length > 0 || "Please provide a value" ] : []
        }
    }
  }
</script>