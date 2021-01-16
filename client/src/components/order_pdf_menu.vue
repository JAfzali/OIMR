<template>
  <v-row align="center" justify="space-around">
    <v-btn
      :loading="recpdfload"
      depressed
      color="white"
      block
      @click="getReceivedPDF"
    >
      Receive
    </v-btn>
    <v-btn
      :loading="orderpdfload"
      depressed
      color="white"
      block
      @click="getOrderPDF"
    >
      Order Confirmation
    </v-btn>
    <v-btn depressed color="white" block @click="getCOC_MC">
      COC Machining
    </v-btn>
    <v-btn depressed color="white" block @click="getCOC_HB">
      COC Hardbanding
    </v-btn>
    <v-btn
      :loading="preinvpdfload"
      depressed
      color="white"
      block
      @click="getPreinvPDF"
    >
      Pre Invoice
    </v-btn>
    <v-btn
      :loading="insprepload"
      depressed
      color="white"
      block
      @click="getInspRepPDF"
    >
      Inspection Report
    </v-btn>
  </v-row>
</template>

<script>
import axios from 'axios'

export default {
  name: 'pdf_menu',
  props: ['currentOrdernr', 'currentrec', 'currentCOCHB', 'currentCOCMC'],
  data() {
    return {
      preinvpdfload: false,
      recpdfload: false,
      orderpdfload: false,
      insprepload: false
    }
  },
  methods: {
    getReceivedPDF() {
      this.recpdfload = true;
      axios
        .get("/getReceivedPDF", {
          params: { receivednr: this.currentrec }
        })
        .then(response => {
          this.recpdfload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    getOrderPDF() {
      this.orderpdfload = true;
      axios
        .get("/getOrderPDF", {
          params: { orderno: this.currentOrdernr }
        })
        .then(response => {
          this.orderpdfload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    getCOC_HB() {
      window.open(this.currentCOCHB, "_blank");
    },
    getCOC_MC() {
      window.open(this.currentCOCMC, "_blank");
    },
    getPreinvPDF() {
      this.preinvpdfload = true;
      axios
        .get("/getPreinvPDF", {
          params: { orderno: this.currentOrdernr }
        })
        .then(response => {
          this.preinvpdfload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    getInspRepPDF() {
      this.insprepload = true;
      axios
        .get("/getdpPDF", {
          params: { orderno: this.currentOrdernr }
        })
        .then(response => {
          this.insprepload = false;
          window.open(response.data.pdflink, "_blank");
        });
    }
  }
}
</script>

<style scoped>

</style>
