```yaml
### Note down a book to read
  - trigger: '~book'
    replace: '- [ ] $|$ #to-read #📙'

### Note down an article to read
  - trigger: '~article'
    replace: '- [ ] $|$ #to-read #📝'

### Note down something to watch
  - trigger: '~watch'
    replace: '- [ ] $|$ #to-watch'

### Capture a quote inline
  - trigger: '~quote'
    replace: '[Quote:: $|$]'

### Create a thought inline
  - trigger: '~thought'
    replace: '[💭 Thought:: $|$]'

### Create an idea inline
  - trigger: '~idea'
    replace: '[💡 Idea:: $|$]'

## Tasks
### Create a task
  - trigger: '~qt'
    replace: '- [ ] #task '

## DATES

  - trigger: '~dnow'
    replace: '{{today}}'
    vars:
      - name: today
        type: date
        params:
          format: '%d/%m/%Y'

  - trigger: '~d1'
    replace: '{{calc_date}}'
    vars:
      - name: calc_date
        type: date
        params:
          format: "%Y-%m-%d"
          offset: 86400

  - trigger: '~d2'
    replace: '{{calc_date}}'
    vars:
      - name: calc_date
        type: date
        params:
          format: "%Y-%m-%d"
          offset: 172800

  - trigger: '~d3'
    replace: '{{calc_date}}'
    vars:
      - name: calc_date
        type: date
        params:
          format: "%Y-%m-%d"
          offset: 259200

  - trigger: '~d4'
    replace: '{{calc_date}}'
    vars:
      - name: calc_date
        type: date
        params:
          format: "%Y-%m-%d"
          offset: 345600

  - trigger: '~d5'
    replace: '{{calc_date}}'
    vars:
      - name: calc_date
        type: date
        params:
          format: "%Y-%m-%d"
          offset: 432000

  - trigger: '~d6'
    replace: '{{calc_date}}'
    vars:
      - name: calc_date
        type: date
        params:
          format: "%Y-%m-%d"
          offset: 518400

  - trigger: '~d7'
    replace: '{{calc_date}}'
    vars:
      - name: calc_date
        type: date
        params:
          format: "%Y-%m-%d"
          offset: 604800

  ## With due icon
  - trigger: '~duetoday'
    replace: '📅 {{today}}'
    vars:
      - name: today
        type: date
        params:
          format: '%d/%m/%Y'

  - trigger: '~due1'
    replace: '📅 {{calc_date}}'
    vars:
      - name: calc_date
        type: date
        params:
          format: "%Y-%m-%d"
          offset: 86400

  - trigger: '~due2'
    replace: '📅 {{calc_date}}'
    vars:
      - name: calc_date
        type: date
        params:
          format: "%Y-%m-%d"
          offset: 172800

  - trigger: '~due3'
    replace: '📅 {{calc_date}}'
    vars:
      - name: calc_date
        type: date
        params:
          format: "%Y-%m-%d"
          offset: 259200

  - trigger: '~due4'
    replace: '📅 {{calc_date}}'
    vars:
      - name: calc_date
        type: date
        params:
          format: "%Y-%m-%d"
          offset: 345600

  - trigger: '~due5'
    replace: '📅 {{calc_date}}'
    vars:
      - name: calc_date
        type: date
        params:
          format: "%Y-%m-%d"
          offset: 432000

  - trigger: '~due6'
    replace: '📅 {{calc_date}}'
    vars:
      - name: calc_date
        type: date
        params:
          format: "%Y-%m-%d"
          offset: 518400

  - trigger: '~due7'
    replace: '📅 {{calc_date}}'
    vars:
      - name: calc_date
        type: date
        params:
          format: "%Y-%m-%d"
          offset: 604800
```