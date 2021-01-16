<template>
  <v-footer
    color="#377AC8"
    app
    dark
    absolute
    height="86px"
  >
    <span class="white--text">&copy; OCEAN IMR AS</span>
    <v-card
      flat
      tile
      width="80%"
      height="50px"
      color="#377AC8"
    >
      <v-card-text>
        <v-btn
          v-for="icon in icons"
          :key="icon"
          class="mx-4"
          icon
          color="white"
        >
          <v-icon size="24px">{{ icon }}</v-icon>
        </v-btn>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  name: 'bottombar',
  data () {
    return {
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram'
      ]
    }
  }
}
</script>

<style lang="css" scoped>
</style>
