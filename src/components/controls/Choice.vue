<template>
    <v-item v-slot:default="{ active, toggle }" :value="value">
        <v-card :color="active ? 'primary' : 'white lighten-3'" @click="toggle(); value.selected = !active">
            <div class="d-flex flex-no-wrap align-center">
                <v-avatar class="ma-3" size="125" tile>
                    <v-icon x-large v-if="imgSrc === undefined">mdi-selection-ellipse</v-icon>
                    <v-img v-else :src="imgSrc" :alt="imgAlt"></v-img> 
                </v-avatar>
                <div>
                    <v-card-title  class="headline" v-text="label"></v-card-title>
                </div>
            </div>
        </v-card>
    </v-item>
</template>

<script>
  export default {
    name: 'Choice',
    props: ['value','label','imgSrc','imgAlt']
  }
</script>