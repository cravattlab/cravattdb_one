var gulp = require('gulp');
var inject = require('gulp-inject');
var bowerFiles = require('main-bower-files');

var pathTo = {
    bowerFiles: './static/bower_components'
};

gulp.task('bowerDeps', function() {
    return gulp.src('./templates/index.html')
        .pipe(inject(gulp.src(bowerFiles(), { read: false }), { 
            name: 'bower'
        }))
        .pipe(gulp.dest('./templates'));
});

gulp.task('watch', function() {
    gulp.watch(pathTo.bowerFiles, ['bowerDeps']); 
});

gulp.task('default', ['bowerDeps', 'watch']);