
class Empty
    def intersectTo f
        self
    end

    def intersectToPoints v
        Empty.new
    end

    def intersectToRay v
        Empty.new
    end

    def intersectToSegment v
        Empty.new
    end
end

# Implement classes
class Points
    attr_accessor :points
    def initialize array
        @points = array.sort
    end

    def intersectTo f
      f.intersectToPoints self
    end

    def intersectToPoints f
      a = f.points & self.points
      if (a == [])
        return Empty.new
      else 
        return Points.new(a)
      end
    end

    def intersectToSegment f
      a=*(f.left..f.right)
      b = a & self.points
      if (b == [])
        return Empty.new
      else 
        return Points.new(b)
      end
    end
    # add more methods

    def intersectToRay f
      self.points = self.points.sort
      seg = Segment.new(self.points[0], self.points[self.points.length - 1])
      res = seg.intersectTo f
      return self.intersectTo res
    end
end

class Segment
  attr_accessor :left, :right
  def initialize(l,r)
    if (l < r)
      @right = r
      @left = l
    else
      @right = l
      @left = r
    end
  end

  def intersectTo f
    f.intersectToSegment self
  end

  def intersectToPoints f
    f.intersectToSegment self
  end

  def intersectToSegment f
    a = *(f.left..f.right)
    b = *(self.left..self.right)
    c = (a & b)
    if (c.length > 1)
      c = c.sort
      return Segment.new(c[0], c[c.length - 1])
    elsif(c.length == 1) 
      return Points.new([c[0]])
    elsif(c.length == 0)
      return Empty.new
    end
  end

  def intersectToRay f
    if((f.center > self.right and f.dir == 1) or ((f.center < self.left and f.dir == -1)))
      return Empty.new
    elsif ((f.center == self.left and f.dir == -1) or (f.center == self.right and f.dir == 1))
      return Points.new([f.center])
    elsif (f.center < self.right and f.dir == 1)
        point = f.center
        while (point < self.left)
          point +=1
        end
        return Segment.new(point, self.right)
    elsif (f.center > self.left and f.dir == -1)
        point = f.center
        while (point < self.right)
          point -=1
        end
        return Segment.new(self.left, point)
    end
  end

end

class Ray
  attr_accessor :dir, :center
  def initialize(center,dir)
      @dir = dir
      @center = center
  end

  def intersectTo f
      f.intersectToRay self
  end

  def intersectToSegment f
      f.intersectToRay self
  end

  def intersectToPoints f
      f.intersectToRay self
  end

  def intersectToRay f

  end


end
