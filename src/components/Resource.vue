<template>
    <v-card>
        <div class="d-flex flex-no-wrap align-center">
            <v-avatar v-if="img.src" class="ma-3" size="125" tile>
                <v-img :src="display(img.src)" :alt="img.alt"></v-img>
            </v-avatar>
            <div class="text-left">
                <v-card-title class="headline" v-text="doc.name"/>
                <v-card-subtitle  v-html="doc.content"/>
            </div>
        </div>
        <v-card-actions>
            <v-btn
              role="button"
              class="success"
              :href="doc.moreInfoUrl"
              :disabled="doc.moreInfoUrl === undefined"
              target="_blank">
                Continue to website<v-icon>mdi-open-in-new</v-icon>
            </v-btn>  
        </v-card-actions>
    </v-card>
</template>

<script>
import image from '@/js/image.js'
export default {
    name: "Resource",
    props: ['doc'],
    data () {
      return {
        endpoint: process.env.VUE_APP_API_ENDPOINT
      }
    },
    computed: {
      img() {
        if (this.doc.img)
          return this.doc.img
        return {
          src: null,
          alt: null
        }
      }
    },
    methods: {
      display(filename) {
        return image(this.endpoint,filename)
      }
    }
};
</script>

<style scoped></style>
