<template>
    <v-card>
        <div class="d-flex flex-no-wrap align-center">
            <v-avatar class="ma-3" size="125" tile>
                <v-skeleton-loader type="avatar"/>
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
export default {
    name: "Resource"
};
</script>

<style scoped></style>
