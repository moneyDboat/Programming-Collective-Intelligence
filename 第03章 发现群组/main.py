from ch03 import clusters, downloadzebodata, generatefeedvector


# main code
print('<----Hierarchical Clustering---->')
blognames, words, data = clusters.readfile('data/blogdata.txt')
clust = clusters.hcluster(data)
clusters.printclust(clust, labels=blognames)

print('<----Drawing the Dendrogram---->')
clusters.drawdendrogram(clust, blognames, jpeg='output/blogclust.jpg')

print('<----Column Clustering---->')
rdata = clusters.rotatematrix(data)
wordclust = clusters.hcluster(rdata)
clusters.drawdendrogram(wordclust, labels=words, jpeg='output/wordclust.jpg')

print('<----K-Means Clustering---->')
kclust, dis_sum = clusters.kcluster(data, k=10)
print([blognames[r] for r in kclust[0]])

print('<----Clusters of Preferences---->')
wants, people, data = clusters.readfile('data/zebo.txt')
clust = clusters.hcluster(data, distance=clusters.tanamoto)
clusters.drawdendrogram(clust, wants, jpeg='output/wants.jpg')

# ex04
clust_manhattan = clusters.hcluster(data, distance=clusters.manhattan)
clusters.drawdendrogram(clust, wants, jpeg='output/wants_manhattan.jpg')

print('<----Viewing Data in Two Dimensions---->')
blognames, words, data = clusters.readfile('data/blogdata.txt')
coords = clusters.scaledown(data)
clusters.draw2d(coords, blognames, jpeg='output/blogs2d.jpg')
