<template>  
    <v-dialog persistent :input="change" :fullscreen="fullscreen" id="modal-dialog" v-model="dialog" width="500px">
        <v-card>
            <v-card-title 
              ref="dialog-title"
              id="dialog-title" 
              role="heading" 
              aria-level="3" 
              class="text-h4 mb-2"
              tabindex="0"
              v-html="title"
            ></v-card-title>
            <v-card-text 
              id="dialog-content"
              tabindex="0"
              v-html="message"
            ></v-card-text>
            <v-card-actions>
              <v-btn 
                role="button" 
                v-for="(btn, index) in buttons" 
                :key="index" 
                text @click="choose(index)">{{btn}}
              </v-btn>
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
    created() {
      this.$nextTick(()=> {
          this.$refs[`dialog-title`].focus()
      })
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

<style scoped>
  .v-dialog__content {
    background-color: rgba(33, 33, 33, 0.7);
  }
</style>