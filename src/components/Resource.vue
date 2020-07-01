<template>
    <v-card>
        <div class="d-flex flex-no-wrap align-center">
            <v-avatar class="ma-3" size="125" tile>
                <v-skeleton-loader v-if="$attrs.doc.img.src === undefined" type="avatar"/>
                <v-img v-else :src="display($attrs.doc.img.src)" :alt="$attrs.doc.img.alt"></v-img>
            </v-avatar>
            <div class="text-left">
                <v-card-title class="headline" v-text="$attrs.doc.name"/>
                <v-card-subtitle  v-html="$attrs.doc.content"/>
            </div>
        </div>
        <v-card-actions>
            <v-btn class="success" text>
                Continue to website<v-icon>mdi-open-in-new</v-icon>
            </v-btn>  
        </v-card-actions>
    </v-card>
</template>

<script>
import image from '@/js/image.js'
export default {
    name: "Resource",
    data () {
      return {
        endpoint: process.env.VUE_APP_API_ENDPOINT
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
