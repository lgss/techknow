<template>
    <v-card
        class="d-flex mx-auto"
        :color="active ? activeColor : 'grey lighten-3'"
        
    >
        <v-container>
            <v-row justify="space-between">
                <v-col cols="auto">
                    <v-img
                        width="100"
                        height="100"
                        src="https://cdn.vuetifyjs.com/images/cards/store.jpg"
                    ></v-img>
                </v-col>

                <v-col cols="auto" class="text-center pl-0">
                    <v-row
                        class="flex-column ma-0 fill-height"
                        justify="center"
                    >
                        <v-col class="px-0">
                            <v-btn icon>
                                <v-icon>mdi-heart</v-icon>
                            </v-btn>
                        </v-col>

                        <v-col class="px-0">
                            <v-btn icon>
                                <v-icon>mdi-bookmark</v-icon>
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</template>

<script>
export default {
    name: "journey",
    props: ["value", "active", "activeColor"]
};
</script>
