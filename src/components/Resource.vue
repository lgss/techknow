<template>
    <v-card height="100%" class="d-flex flex-column justify-space-between">
        <div class="d-flex flex-no-wrap align-center">
            <v-img v-if="img.src" class="ma-3" :src="display(img.src)" :alt="img.alt" max-width="125" max-height="125"></v-img>
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
              v-if="doc.moreInfoUrl"
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
