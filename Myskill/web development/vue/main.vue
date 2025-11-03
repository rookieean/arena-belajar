<template>
    <div>
        <app-header></app-header>
            <div class="container"
                <ul>
                    <li>Honda</li>
                    <li>Toyota</li>
                    <li>Ford</li>
                </ul>
        <app-footer></app-footer>
    </div>
    </div>
</template>





<script>
import { Component } from 'react';


export default {
    Components: {
        compBrand
    },

    data() {
        return {
            cars: [
                {model: 'Jazz', brand: 'Honda'},
                {model: 'Yaria', brand: 'Toyota'},
                {model: 'Airew', brand: 'Mulling'},
            ]
        }
    },
}

provide() {
    
}

</script>