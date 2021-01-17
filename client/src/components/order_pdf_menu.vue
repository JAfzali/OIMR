<template>
    <v-dialog v-model="dialog" width="350">
      <v-card>
        <v-list-item two-line class="light-blue lighten-4">
          <v-list-item-content>
            <v-list-item-title class="headline"></v-list-item-title>
            <v-list-item-subtitle>Order Numbers</v-list-item-subtitle>
            <v-list-item-title class="headline">{{
                currentOrdernr
              }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <div :class="padding_class">
          <v-btn
            :loading="recpdfload"
            depressed
            color="white"
            block
            @click="getReceivedPDF"
          >
            Receive
            <v-spacer/>
          </v-btn>
          <v-btn
            :loading="orderpdfload"
            depressed
            color="white"
            block
            @click="getOrderPDF"
          >
            Order Confirmation
            <v-spacer/>
          </v-btn>
          <v-btn depressed color="white" block @click="getCOC_MC">
            COC Machining
            <v-spacer/>
          </v-btn>
          <v-btn depressed color="white" block @click="getCOC_HB">
            COC Hardbanding
            <v-spacer/>
          </v-btn>
          <v-btn
            :loading="preinvpdfload"
            depressed
            color="white"
            block
            @click="getPreinvPDF"
          >
            Pre Invoice
            <v-spacer/>
          </v-btn>
          <v-btn
            :loading="insprepload"
            depressed
            color="white"
            block
            @click="getInspRepPDF"
          >
            Inspection Report
            <v-spacer/>
          </v-btn>
        </div>
      </v-card>
    </v-dialog>
</template>

<script>
import axios from 'axios'

export default {
  name: 'pdf_menu',
  props: ['currentOrdernr', 'currentrec', 'currentCOCHB', 'currentCOCMC', 'dialog'],
  data() {
    return {
      preinvpdfload: false,
      recpdfload: false,
      orderpdfload: false,
      insprepload: false,
      padding_class: 'pl-2'
    }
  },
  watch: {
    dialog(value) {
      console.log(value)
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
