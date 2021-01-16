<template>
  <v-container >
    <v-card  elevation="0">
      <v-list-item two-line class="white">
        <v-list-item-content>
          <v-list-item-title class="headline"><b>{{
            getUsername
          }}</b></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-row >
        <v-col v-for="card in getAssetlist" :key="card" :cols="6">
          <v-card @click="test(card)" height="200" dark color="#204060">
            <v-card-title primary-title class="justify-center">
              <div>
                <h1 class="headline">{{card}}</h1>
              </div>
            </v-card-title>
          </v-card>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>
<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: "asset",
  data() {
    return {};
  },
  methods: {
    ...mapActions(['setasset']),
    test(card)  {
      console.log(card)
      this.setasset({ asset: card })
      this.$router.replace('home')
    }
  },
  mounted() {
    console.log("ponde");
  },
  computed: {
    ...mapGetters(["getUsername", "getAssetlist"])
  }
};
</script>
<style lang="css" scoped>
</style>