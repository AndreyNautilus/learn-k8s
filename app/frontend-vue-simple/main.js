const app = Vue.createApp({
    data() {
        return {
            messages: [
                {
                    'author': 'fe user 1',
                    'message': 'fe message 1'
                },
                {
                    'author': 'fe user 2',
                    'message': 'fe message 2'
                },
                {
                    'author': 'fe user 3',
                    'message': 'fe message 3'
                }
            ],
            backendWorker: 'no backend'
        }
    }
})
