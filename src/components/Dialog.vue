<template>  
    <v-dialog persistent @input="change" @fullscreen="fullscreen" id="modal-dialog" v-model="dialog" width="500px">
      <v-card>
          <v-card-title>{{title}}</v-card-title>
          <v-card-text>{{message}}</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn v-for="(btn, index) in buttons" :key="index" text @click="choose(index)">{{btn}}</v-btn>
          </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
export default {
    props: {
      'buttons': {
          type: Array
      },
      'title': {type: String},
      'message': {type: String}, 
      'fullscreen': {
          type: Boolean,
          default: false
      }
    },
    methods: {
      choose(value) {
        this.$emit('result', value)
        this.value = value
        this.$destroy()
      },
      change() {
        this.$destroy()
      }
    },
    data() {
        return {
            dialog: true
        }
    }
}
</script>